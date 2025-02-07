import CoreML
import Foundation

public enum TokenML {
    static let tokensModel: MLModel? = {
        let configuration = MLModelConfiguration()
        configuration.computeUnits = .all

        guard let modelUrl = Bundle.module.url(forResource: "Tokens", withExtension: "mlmodelc") else {
            return nil
        }

        return try? MLModel(contentsOf: modelUrl, configuration: configuration)
    }()
}
