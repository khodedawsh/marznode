# Multi-stage build: equip marznode with sing-box v1.13.12.
#
# Stage 1 builds sing-box from source because the official
# ghcr.io/sagernet/sing-box:latest image ships without the
# `with_v2ray_api` and `with_grpc` tags — marznode needs the former for
# user-traffic stats (FetchUsersStats) and the latter for v2ray grpc
# transports.

FROM golang:1.25-alpine AS singbox-builder

ARG SING_BOX_VERSION=v1.13.12
# Tag parity with dawsh/marznode's sing-box 1.11.3 build, minus tags that
# became implicit in 1.13.x (with_reality_server → with_utls, with_ech →
# stdlib). `with_musl` mirrors the official alpine-based release.
ARG SING_BOX_TAGS="with_gvisor,with_quic,with_grpc,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_v2ray_api,with_musl,badlinkname,tfogo_checklinkname0"

RUN apk add --no-cache git

RUN git clone --depth 1 --branch "${SING_BOX_VERSION}" \
        https://github.com/SagerNet/sing-box.git /src
WORKDIR /src

# -checklinkname=0 / -X internal/godebug.defaultGODEBUG=multipathtcp=0
# mirror release/LDFLAGS from upstream. Without -checklinkname=0 Go 1.23+
# rejects sing-box's linkname hooks into crypto/tls internals ("invalid
# reference to handlePostHandshakeMessage"). GOTOOLCHAIN=local pins us to
# the image's Go (go.mod may request a newer patch version).
RUN GOTOOLCHAIN=local CGO_ENABLED=0 go build -trimpath \
        -ldflags "-s -w -buildid= -checklinkname=0 -X internal/godebug.defaultGODEBUG=multipathtcp=0 -X github.com/sagernet/sing-box/constant.Version=${SING_BOX_VERSION}" \
        -tags "${SING_BOX_TAGS}" \
        -o /out/sing-box \
        ./cmd/sing-box

# Sanity-check that the produced binary has all the tags we asked for.
 RUN version_output="$("/out/sing-box" version)" \
         && printf '%s\n' "${version_output}" \
         && for tag in $(printf '%s' "${SING_BOX_TAGS}" | tr ',' ' '); do \
              printf '%s\n' "${version_output}" | grep -F -q -- "${tag}" \
                || { echo "missing build tag in /out/sing-box: ${tag}" >&2; exit 1; }; \
            done


FROM tobyxdd/hysteria:v2 AS hysteria-image

FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

COPY --from=hysteria-image /usr/local/bin/hysteria /usr/local/bin/hysteria
COPY --from=singbox-builder /out/sing-box /usr/local/bin/sing-box

WORKDIR /app

COPY . .

RUN mkdir /etc/init.d/

RUN apk add --no-cache curl unzip

RUN curl -L -H "Cache-Control: no-cache" -o xray.zip https://github.com/XTLS/Xray-core/releases/latest/download/Xray-linux-64.zip && \
    unzip xray.zip -d /usr/local/bin/ && \
    rm -f xray.zi

# Download the GeoIP and GeoSite routing databases
RUN mkdir -p /usr/local/lib/xray && \
    curl -L -o /usr/local/lib/xray/geoip.dat https://github.com/v2fly/geoip/releases/latest/download/geoip.dat && \
    curl -L -o /usr/local/lib/xray/geosite.dat https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat

RUN apk add --no-cache alpine-sdk libffi-dev && pip install --no-cache-dir -r /app/requirements.txt && apk del -r alpine-sdk libffi-dev curl unzip

CMD ["python3", "marznode.py"]