use std::collections::HashMap;
use uuid::Uuid;
use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IntentNode {
    pub id: String,
    pub action: String,
    pub params: HashMap<String, serde_json::Value>,
    pub children: Vec<String>,
}

pub struct IntentGraph {
    nodes: HashMap<String, IntentNode>,
}

impl IntentGraph {
    pub fn new() -> Self {
        IntentGraph { nodes: HashMap::new() }
    }

    pub fn add_intent(&mut self, action: &str, params: HashMap<String, serde_json::Value>) -> String {
        let id = Uuid::new_v4().to_string();
        self.nodes.insert(id.clone(), IntentNode {
            id: id.clone(),
            action: action.to_string(),
            params,
            children: vec![],
        });
        id
    }

    pub fn resolve_intent(&self, id: &str) -> Option<&IntentNode> {
        self.nodes.get(id)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_add_and_resolve() {
        let mut graph = IntentGraph::new();
        let id = graph.add_intent("create_report", HashMap::new());
        assert!(graph.resolve_intent(&id).is_some());
    }
}
