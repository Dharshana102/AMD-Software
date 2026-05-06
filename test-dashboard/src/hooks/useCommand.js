import { useCallback } from 'react';
import { useDashboard } from '../context/DashboardContext';

export function useCommand() {
  const { addLog } = useDashboard();

  const sendCommand = useCallback(async (action, params = {}) => {
    /* 
      Replace this function body with your actual serial / API call.
      It currently simulates a 0.5-1.5 s round-trip.
    */
    addLog(`TX → ${action}  ${JSON.stringify(params)}`, 'info');
    
    return new Promise(resolve => {
      const delay = 500 + Math.random() * 1000;
      setTimeout(() => {
        const ok = Math.random() > 0.15; // 85% success for demo
        if (ok) {
          addLog(`RX ← ${action}  OK`, 'ok');
          resolve({ ok: true, data: `${action} completed` });
        } else {
          addLog(`RX ← ${action}  ERROR: timeout`, 'err');
          resolve({ ok: false, error: 'timeout' });
        }
      }, delay);
    });
  }, [addLog]);

  return { sendCommand };
}

