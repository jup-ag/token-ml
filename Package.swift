// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "TokenML",
    platforms: [
        .iOS(.v17)
    ],
    products: [
        .library(name: "TokenML", targets: ["TokenML"])
    ],
    dependencies: [
    ],
    targets: [
        .target(
            name: "TokenML",
            path: "TokenML",
            resources: [
                .process("Generated/Tokens.mlmodel")
            ]
        )
    ]
)
