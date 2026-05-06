import { useEffect, useCallback } from 'react';
import { useDashboard } from '../context/DashboardContext';
import { MODULES } from '../data/modulesData';
 
export function useModuleStatus() {
  const { setModuleStatus, setConnectionStatus } = useDashboard();
 
  const pollModuleStatus = useCallback(() => {
    /* Replace with real heartbeat / ping logic */
    MODULES.forEach(m => {
      // Set all modules to 'online' for static display
      const status = 'online'; // ← Changed from random to static
      setModuleStatus(m.id, status);
    });
  }, [setModuleStatus]);
 
  useEffect(() => {
    // Initial check only
    const initialTimer = setTimeout(pollModuleStatus, 600);
    const connTimer = setTimeout(() => setConnectionStatus(true), 1000);
    // Comment out or remove the interval to stop polling
    // const interval = setInterval(pollModuleStatus, 10000);
 
    return () => {
      clearTimeout(initialTimer);
      clearTimeout(connTimer);
      // clearInterval(interval);
    };
  }, [pollModuleStatus, setConnectionStatus]);
}