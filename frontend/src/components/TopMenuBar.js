import React from "react";
import {
  AppBar,
  IconButton,
  Menu,
  MenuItem,
  Toolbar,
  Typography,
} from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";

const TopMenuBar = () => {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleMenuClose = () => {
    setAnchorEl(null);
  };
  return (
    <AppBar position="static">
      <Toolbar>
        <IconButton edge="start" onClick={handleMenuOpen}>
          <MenuIcon />
        </IconButton>
        <Menu
          anchorEl={anchorEl}
          keepMounted
          open={Boolean(anchorEl)}
          onClose={handleMenuClose}
        >
          <MenuItem onClick={handleMenuClose}>
            <Link to="/">Home</Link>
          </MenuItem>
          <MenuItem onClick={handleMenuClose}>
            <Link to="/form">Form</Link>
          </MenuItem>
          <MenuItem onClick={handleMenuClose}>
            <Link to="/file">File</Link>
          </MenuItem>
          <MenuItem onClick={handleMenuClose}>
            <Link to="/download">Download</Link>
          </MenuItem>
          <MenuItem onClick={handleMenuClose}>
            <Link to="/data">Data</Link>
          </MenuItem>
        </Menu>
        <Typography variant="h6">Frontend</Typography>
      </Toolbar>
    </AppBar>
  );
};

export default TopMenuBar;
