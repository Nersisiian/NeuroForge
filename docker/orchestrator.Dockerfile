FROM rust:1.85-slim-bookworm as builder
RUN apt-get update && apt-get install -y protobuf-compiler && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:bookworm-slim
COPY --from=builder /app/target/release/neuroforge-orchestrator /usr/local/bin/orchestrator
EXPOSE 8080
CMD ["orchestrator"]
