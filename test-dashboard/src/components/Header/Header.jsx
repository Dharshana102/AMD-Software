import React from 'react';
import { useDashboard } from '../../context/DashboardContext';
import './Header.css';

function Header() {
  const { isConnected } = useDashboard();

  return (
    <header className="header">
      <h1 className="header-title">Dashboard</h1>
      <div className="header-right">
        <div className="conn-status">
          <div className={`conn-dot ${isConnected ? 'online' : ''}`}></div>
          <span className="conn-label">
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
      </div>
    </header>
  );
}

export default Header;
  
