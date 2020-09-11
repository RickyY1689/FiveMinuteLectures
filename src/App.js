import React from 'react';
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Summarizer from './components/Summarizer'
import {Box, Grid, Paper} from '@material-ui/core'


const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
  input: {
    display: 'none',
  },
  container: {
    display: 'flex',
    alignItems: 'center',
    flexDirection: 'column'
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  photo: {
    maxHeight: "60%",
    maxWidth: "60%"
  }
}));

const App = () => {
  const classes = useStyles();

  return (
    <Grid container spacing={2}>
      <Grid item xs={2}/>
      <Grid item xs={8}>
        <Box my={5} className={classes.container}>
          <img src={require("./images/logo.png")} className={classes.photo}/>
        </Box>
        <Box mt={20} borderRadius={50} bgcolor="white">
          <Summarizer/>
        </Box>
      </Grid>
      <Grid item xs={2}/>
    </Grid>
  );
}

export default App;
