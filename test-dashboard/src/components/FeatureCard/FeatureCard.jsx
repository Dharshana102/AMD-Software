import React, { useState, useCallback } from 'react';
import { useDashboard } from '../../context/DashboardContext';
import { useCommand } from '../../hooks/useCommand';
import StatusIndicator from '../StatusIndicator/StatusIndicator';
import SelectControl from '../Controls/SelectControl';
import ToggleControl from '../Controls/ToggleControl';
import ButtonControl from '../Controls/ButtonControl';
import InfoDisplayControl from '../Controls/InfoDisplayControl';
import './FeatureCard.css';

function FeatureCard({ feature, moduleStatus }) {
  const { featureStatus, setFeatureStatus, toggleState, setToggleState } = useDashboard();
  const { sendCommand } = useCommand();
  const [selectValues, setSelectValues] = useState({});
  const [dynamicValues, setDynamicValues] = useState({});

  const status = featureStatus[feature.id];
  const isOffline = moduleStatus === 'offline';

  const getSelectedTarget = useCallback(() => {
    const selectControl = feature.controls.find(c => c.type === 'select');
    if (selectControl && selectValues[selectControl.id]) {
      return selectValues[selectControl.id];
    }
    return selectControl ? selectControl.options[0] : null;
  }, [feature.controls, selectValues]);

  // Check if dynamic inputs should be shown next to status (angle/time) or below (steps/speed)
  const isStepperCard = feature.id === 'camera_stepper';
  const selectedTarget = getSelectedTarget();

  const handleButtonClick = async (action) => {
    if (action.includes('_copy_')) {
      const infoControl = feature.controls.find(c => c.type === 'info');
      if (infoControl) {
        const fieldType = action.includes('_copy_ip') ? 'ip' : 'mac';
        const field = infoControl.fields.find(f => f.id === fieldType);
        if (field) {
          try {
            await navigator.clipboard.writeText(field.value);
          } catch (err) {
            console.error('Failed to copy:', err);
          }
        }
      }
      return;
    }

    const dynamicControl = feature.controls.find(c => c.type === 'dynamic');
    if (dynamicControl) {
      const target = getSelectedTarget();
      const fields = target
        ? (dynamicControl.fields[target] || dynamicControl.fields['default'] || [])
        : [];

      if (fields.length > 0) {
        const currentDynamicValues = dynamicValues[dynamicControl.id] || {};
        for (const field of fields) {
          const fieldValue = currentDynamicValues[field.id];
          if (!fieldValue || fieldValue === '') {
            alert(`Please enter ${field.label}`);
            return;
          }
          if (field.type === 'number') {
            const numValue = parseFloat(fieldValue);
            if (isNaN(numValue)) {
              alert(`${field.label} must be a valid number`);
              return;
            }
            if (numValue < field.min || numValue > field.max) {
              alert(`${field.label} must be between ${field.min} and ${field.max}`);
              return;
            }
          }
        }
      }
    }

    const params = { ...selectValues, ...dynamicValues };
    setFeatureStatus(feature.id, 'running');
    const res = await sendCommand(action, params);
    setFeatureStatus(feature.id, res.ok ? 'pass' : 'fail');
  };

  // For icon toggle buttons like Mute/Unmute and Play/Pause
  const handleToggleButtonClick = async (button) => {
    const currentState = toggleState[button.stateKey] || false;
    const actionToSend = currentState ? button.activeAction : button.action;

    setFeatureStatus(feature.id, 'running');
    const res = await sendCommand(actionToSend);

    if (res.ok) {
      setToggleState(button.stateKey, !currentState);
      setFeatureStatus(feature.id, 'pass');
    } else {
      setFeatureStatus(feature.id, 'fail');
    }
  };

  const handleToggle = async (controlId, actionOn, actionOff) => {
    const currentState = toggleState[controlId] || false;
    const newState = !currentState;
    const action = newState ? actionOn : actionOff;

    setFeatureStatus(feature.id, 'running');
    const res = await sendCommand(action);

    if (res.ok) {
      setToggleState(controlId, newState);
      setFeatureStatus(feature.id, 'pass');
    } else {
      setFeatureStatus(feature.id, 'fail');
    }
  };

  const handleSelectChange = (controlId, value) => {
    setSelectValues(prev => ({ ...prev, [controlId]: value }));
  };

  const handleDynamicChange = (controlId, fieldId, fieldValue) => {
    setDynamicValues(prev => ({
      ...prev,
      [controlId]: {
        ...(prev[controlId] || {}),
        [fieldId]: fieldValue
      }
    }));
  };

  // Find controls by type
  const selectControls = feature.controls.filter(c => c.type === 'select');
  const dynamicControls = feature.controls.filter(c => c.type === 'dynamic');
  const infoControls = feature.controls.filter(c => c.type === 'info');
  const toggleControls = feature.controls.filter(c => c.type === 'toggle');
  const buttonControls = feature.controls.filter(c => c.type === 'buttons');

  return (
    <div className="feature-card">
      <div className="feature-title">{feature.title}</div>
      <div className="feature-desc">{feature.desc}</div>

      {/* Status + Small Inline Inputs (for angle/time next to status) */}
      {!isStepperCard && (
        <div className="f-status-row">
          <StatusIndicator status={status} />
          {dynamicControls.map(dc => {
            const targetFields = selectedTarget
              ? (dc.fields[selectedTarget] || dc.fields['default'] || [])
              : [];

            return (
              <div key={dc.id} className="dynamic-input-inline">
                {targetFields.map(field => {
                  const currentValues = dynamicValues[dc.id] || {};
                  return (
                    <div key={field.id} className="input-group-inline">
                      <input
                        type={field.type === 'number' ? 'number' : 'text'}
                        className="param-input-inline"
                        min={field.min}
                        max={field.max}
                        placeholder={field.placeholder}
                        value={currentValues[field.id] || ''}
                        onChange={(e) => handleDynamicChange(dc.id, field.id, e.target.value)}
                      />
                    </div>
                  );
                })}
              </div>
            );
          })}
        </div>
      )}

      {/* Stepper Card - Show Status alone, then inputs below */}
      {isStepperCard && (
        <>
          <div className="f-status-row">
            <StatusIndicator status={status} />
          </div>

          {dynamicControls.map(dc => {
            const targetFields = dc.fields['default'] || [];
            return (
              <div key={dc.id} className="dynamic-inputs-block">
                {targetFields.map(field => {
                  const currentValues = dynamicValues[dc.id] || {};
                  return (
                    <div key={field.id} className="input-group-inline">
                      <input
                        type={field.type === 'number' ? 'number' : 'text'}
                        className="param-input-inline"
                        min={field.min}
                        max={field.max}
                        placeholder={field.placeholder}
                        value={currentValues[field.id] || ''}
                        onChange={(e) => handleDynamicChange(dc.id, field.id, e.target.value)}
                      />
                    </div>
                  );
                })}
              </div>
            );
          })}
        </>
      )}

      {/* Select controls */}
      {selectControls.map(sc => (
        <SelectControl
          key={sc.id}
          control={sc}
          value={selectValues[sc.id] || sc.options[0]}
          onChange={handleSelectChange}
        />
      ))}

      {/* Info controls */}
      {infoControls.map(ic => (
        <InfoDisplayControl key={ic.id} control={ic} />
      ))}

      {/* Toggle controls */}
      {toggleControls.map(tc => (
        <ToggleControl
          key={tc.id}
          control={tc}
          isOn={toggleState[tc.id] || false}
          onToggle={handleToggle}
        />
      ))}

      {/* Button controls */}
      {buttonControls.map((bc, index) => (
        <ButtonControl
          key={`buttons-${index}`}
          items={bc.items}
          onButtonClick={handleButtonClick}
          onToggleButtonClick={handleToggleButtonClick}
          toggleState={toggleState}
          disabled={isOffline}
        />
      ))}
    </div>
  );
}

export default FeatureCard;