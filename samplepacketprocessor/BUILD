load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@dnos_python_libs//:requirements.bzl", "requirement")

COMPILE_DEPS = [
    "@dnos_core_grpc_python//protobuf/proto:onos-core-protobuf-services-proto",
    requirement("python-openflow"),
    requirement("ryu"),
]

py_binary(
    name = "samplepacketprocessor",
    srcs = ["samplepacketprocessor.py"],
    main = "samplepacketprocessor.py",
    deps = COMPILE_DEPS,
)
