use automerge::AutoCommit;
use automerge::transaction::Transactable;
use automerge::ReadDoc;

pub struct ImmortalStore {
    doc: AutoCommit,
}

impl ImmortalStore {
    pub fn new() -> Self {
        ImmortalStore {
            doc: AutoCommit::new(),
        }
    }

    pub fn set_intent(&mut self, id: &str, value: serde_json::Value) -> Result<(), automerge::AutomergeError> {
        self.doc.put(automerge::ROOT, id, value.to_string())?;
        self.doc.commit(); // просто фиксируем, хеш не нужен
        Ok(())
    }

    pub fn get_intent(&self, id: &str) -> Option<serde_json::Value> {
        if let Some((val, _)) = self.doc.get(automerge::ROOT, id).ok()? {
            match val {
                automerge::Value::Scalar(s) => {
                    Some(serde_json::Value::String(s.to_string()))
                }
                _ => None,
            }
        } else {
            None
        }
    }
}
