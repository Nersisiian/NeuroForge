import { create } from 'zustand';

interface Intent {
  id: string;
  text: string;
  active: boolean;
}

interface IntentStore {
  intents: Intent[];
  sendIntent: (text: string) => Promise<void>;
}

export const useIntentStore = create<IntentStore>((set, get) => ({
  intents: [],
  sendIntent: async (text) => {
    const newIntent: Intent = {
      id: Math.random().toString(36).substring(7),
      text,
      active: true,
    };
    set({ intents: [...get().intents, newIntent] });

    try {
      // ?????? POST, ? ?????
      await fetch('http://localhost:8000/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
    } catch (e) {
      console.error('Cortex request failed:', e);
    }

    // ???????????? ???? ????? 5 ??????
    setTimeout(() => {
      set((state) => ({
        intents: state.intents.map((i) =>
          i.id === newIntent.id ? { ...i, active: false } : i
        ),
      }));
    }, 5000);
  },
}));
