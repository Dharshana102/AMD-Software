import React from 'react';
import { DashboardProvider } from './context/DashboardContext';
import Header from './components/Header/Header';
import Sidebar from './components/Sidebar/Sidebar';
import MainPanel from './components/MainPanel/MainPanel';
import { useModuleStatus } from './hooks/useModuleStatus';
import './App.css';

function AppContent() {
  useModuleStatus();

  return (
    <div className="app">
      <Header />
      <div className="container">
        <Sidebar />
        <MainPanel />
      </div>
    </div>
  );
}

function App() {
  return (
    <DashboardProvider>
      <AppContent />
    </DashboardProvider>
  );
}

export default App;
