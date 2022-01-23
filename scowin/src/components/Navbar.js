import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as FiIcons from 'react-icons/fi';
import { Link } from 'react-router-dom';
import './Navbar.css';
import { IconContext } from 'react-icons';
import logo_image from '../images/scowin_logo_2.png';

function Navbar() {
  const [sidebar, setSidebar] = useState(true);
  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      <IconContext.Provider value={{ color: '#000' }}>
        <div className='navbar'>
          <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar} />
          </Link>
        </div>
        <hr />
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
          <ul className='nav-menu-items' onClick={showSidebar}>
            <li className='navbar-toggle'>
              <Link to='#' className='menu-bars' id="closebutton_1">
                <AiIcons.AiOutlineClose />
              </Link>
              <img src={logo_image} alt='logo_image' className='img3'></img>
              <p className='nav-head1'>Welcome user</p> 
            </li>
            <li key="" className="nav-text" id='first'> 
              <Link to="/"><span><AiIcons.AiFillHome /> Home  </span></Link>
            </li>
            <li key="" className="nav-text"> 
              <Link to="/manageStudent"><span> <FaIcons.FaUserFriends /> Manage Student Details </span></Link>
            </li>
            <li key="" className="nav-text"> 
              <Link to="/vaccination"><span><FaIcons.FaUserMd /> Update Vaccination status </span></Link>
            </li>
            <li key="" className="nav-text"> 
              <Link to=""><span><FaIcons.FaSyringe /> Manage Vaccination drive </span></Link>
            </li>
            <li key="" className="nav-text"> 
              <Link to=""><span><FaIcons.FaClipboardCheck /> Generate Reports </span></Link>
            </li>
            <li key="" className="nav-text"> 
              <Link to=""><span><FiIcons.FiLogOut /> Logout </span></Link>
            </li>
          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
