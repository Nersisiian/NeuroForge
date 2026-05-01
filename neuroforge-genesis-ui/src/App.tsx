import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Environment, Sphere } from '@react-three/drei';
import { useIntentStore } from './store';

function IntentNode({ position, active }: { position: [number, number, number]; active: boolean }) {
  return (
    <mesh position={position}>
      <sphereGeometry args={[0.2, 32, 32]} />
      <meshStandardMaterial color={active ? "hotpink" : "cyan"} />
    </mesh>
  );
}

function DynamicGraph() {
  const intents = useIntentStore((s) => s.intents);
  return (
    <group>
      {intents.map((intent, i) => (
        <IntentNode
          key={intent.id}
          position={[Math.sin(i) * 2, Math.cos(i * 2) * 0.5, -2]}
          active={intent.active}
        />
      ))}
    </group>
  );
}

function App() {
  const sendIntent = useIntentStore((s) => s.sendIntent);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && e.currentTarget.value.trim()) {
      sendIntent(e.currentTarget.value.trim());
      e.currentTarget.value = '';
    }
  };

  return (
    <div style={{ width: '100vw', height: '100vh', background: '#000' }}>
      <Canvas camera={{ position: [0, 0, 5], fov: 60 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <DynamicGraph />
        <OrbitControls enableZoom={true} enablePan={true} />
        <Environment preset="city" />
      </Canvas>
      <div style={{
        position: 'absolute',
        bottom: 30,
        left: '50%',
        transform: 'translateX(-50%)',
        background: 'rgba(0,0,0,0.8)',
        padding: '10px 20px',
        borderRadius: 8,
        border: '1px solid cyan'
      }}>
        <input
          placeholder="????? ?????????, ????????: ????? ?? ????????"
          onKeyDown={handleKeyDown}
          style={{
            width: 350,
            padding: '10px',
            fontSize: 16,
            borderRadius: 6,
            border: 'none',
            outline: 'none',
            background: '#111',
            color: 'white'
          }}
        />
        <span style={{ color: 'white', marginLeft: 10, fontFamily: 'monospace' }}>
          NeuroForge
        </span>
      </div>
    </div>
  );
}

export default App;
