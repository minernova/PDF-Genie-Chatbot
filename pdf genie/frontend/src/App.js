
import React from 'react';
import UploadComponent from './components/UploadComponent';
import DeleteComponent from './components/DeleteComponent';

function App() {
  return (
    <div className="App">
      <h1>PDF Genie Chatbot</h1>
      <UploadComponent />
      <DeleteComponent />
    </div>
  );
}

export default App;
