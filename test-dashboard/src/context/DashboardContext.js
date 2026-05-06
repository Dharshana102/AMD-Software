  import React, { createContext, useContext, useReducer, useCallback } from 'react';
import { MODULES } from '../data/modulesData';

const DashboardContext = createContext();

const initialState = {
  modules: MODULES,
  moduleStatus: {},
  featureStatus: {},
  toggleState: {},
  activeModule: null,
  logEntries: [],
  isConnected: false
};

// Initialize states
MODULES.forEach(m => {
  initialState.moduleStatus[m.id] = 'offline';
  m.features.forEach(f => {
    initialState.featureStatus[f.id] = 'idle';
  });
});

function dashboardReducer(state, action) {
  switch (action.type) {
    case 'SET_MODULE_STATUS':
      return {
        ...state,
        moduleStatus: {
          ...state.moduleStatus,
          [action.payload.id]: action.payload.status
        }
      };
    case 'SET_FEATURE_STATUS':
      return {
        ...state,
        featureStatus: {
          ...state.featureStatus,
          [action.payload.id]: action.payload.status
        }
      };
    case 'SET_TOGGLE_STATE':
      return {
        ...state,
        toggleState: {
          ...state.toggleState,
          [action.payload.id]: action.payload.value
        }
      };
    case 'SET_ACTIVE_MODULE':
      return {
        ...state,
        activeModule: action.payload
      };
    case 'ADD_LOG_ENTRY':
      const newLogs = [...state.logEntries, action.payload];
      if (newLogs.length > 200) newLogs.shift();
      return {
        ...state,
        logEntries: newLogs
      };
    case 'CLEAR_LOGS':
      return {
        ...state,
        logEntries: []
      };
    case 'SET_CONNECTION_STATUS':
      return {
        ...state,
        isConnected: action.payload
      };
    default:
      return state;
  }
}

export function DashboardProvider({ children }) {
  const [state, dispatch] = useReducer(dashboardReducer, initialState);

  const addLog = useCallback((msg, level = 'info') => {
    const ts = new Date().toLocaleTimeString('en-GB', { hour12: false });
    dispatch({
      type: 'ADD_LOG_ENTRY',
      payload: { ts, msg, level }
    });
  }, []);

  const setModuleStatus = useCallback((id, status) => {
    dispatch({ type: 'SET_MODULE_STATUS', payload: { id, status } });
  }, []);

  const setFeatureStatus = useCallback((id, status) => {
    dispatch({ type: 'SET_FEATURE_STATUS', payload: { id, status } });
  }, []);

  const setToggleState = useCallback((id, value) => {
    dispatch({ type: 'SET_TOGGLE_STATE', payload: { id, value } });
  }, []);

  const setActiveModule = useCallback((moduleId) => {
    dispatch({ type: 'SET_ACTIVE_MODULE', payload: moduleId });
  }, []);

  const clearLogs = useCallback(() => {
    dispatch({ type: 'CLEAR_LOGS' });
  }, []);

  const setConnectionStatus = useCallback((status) => {
    dispatch({ type: 'SET_CONNECTION_STATUS', payload: status });
  }, []);

  const value = {
    ...state,
    addLog,
    setModuleStatus,
    setFeatureStatus,
    setToggleState,
    setActiveModule,
    clearLogs,
    setConnectionStatus
  };

  return (
    <DashboardContext.Provider value={value}>
      {children}
    </DashboardContext.Provider>
  );
}

export function useDashboard() {
  const context = useContext(DashboardContext);
  if (!context) {
    throw new Error('useDashboard must be used within a DashboardProvider');
  }
  return context;
}

