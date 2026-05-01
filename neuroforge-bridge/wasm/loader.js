// neuroforge-bridge/wasm/loader.js
export async function loadBridge() {
  const wasm = await import('../../neuroforge-core/pkg/neuroforge_core.js');
  console.log('WASM bridge loaded: intent graph ready');
  return wasm;
}
