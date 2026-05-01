use tonic::transport::Channel;
use cortex::cortex_client::CortexClient;
use cortex::IntentRequest;

pub mod cortex {
    tonic::include_proto!("cortex");
}

pub struct Orchestrator {
    cortex_client: CortexClient<Channel>,
}

impl Orchestrator {
    pub async fn new() -> Result<Self, Box<dyn std::error::Error>> {
        let addr = "http://localhost:50051";
        let client = CortexClient::connect(addr).await?;
        Ok(Orchestrator { cortex_client: client })
    }

    pub async fn process_text(&mut self, text: &str) -> Result<String, Box<dyn std::error::Error>> {
        let req = tonic::Request::new(IntentRequest {
            text: text.to_string(),
            context: std::collections::HashMap::new(),
        });
        let resp = self.cortex_client.parse_intent(req).await?;
        let result = serde_json::json!({
            "action": resp.get_ref().action,
            "params": resp.get_ref().params_json,
            "confidence": resp.get_ref().confidence
        });
        Ok(result.to_string())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[tokio::test]
    async fn test_orchestrator_connection() {
        // This test will only work when cortex is running
        // for now it just ensures the code compiles
    }
}
