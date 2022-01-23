import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes , Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Vaccine from './pages/vaccination';

function App() {
  return (
    <div className="App">
      <Router>
        <div>
          <Navbar />
          <Routes>
            <Route path='/' exact element={<Home />} />
            <Route path='/vaccination' element={<Vaccine />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}
export default App;