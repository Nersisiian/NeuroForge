import React, { useEffect, useRef } from 'react';

export default function FluidCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    async function initGPU() {
      if (!navigator.gpu) {
        console.log('WebGPU не поддерживается — переключись на Chrome Canary, грандмастер');
        return;
      }
      const adapter = await navigator.gpu.requestAdapter();
      const device = await adapter?.requestDevice();
      if (!device) return;
      const context = canvasRef.current?.getContext('webgpu');
      console.log('NeuroForge Fluid Canvas: WebGPU готов к перестройке реальности');
    }
    initGPU();
  }, []);

  return <canvas ref={canvasRef} width={1024} height={768} style={{ border: '2px solid cyan' }} />;
}
