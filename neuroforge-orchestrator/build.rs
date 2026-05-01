fn main() {
    tonic_build::configure()
        .build_server(false)
        .compile(&["proto/cortex.proto"], &["proto/"])
        .unwrap();
}
