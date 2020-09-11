import React, { useState }  from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Box, Button, Typography } from '@material-ui/core';
import axios from 'axios'

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
    justifyContent: 'center',
    flexDirection: 'column'
  }
}));

const Summarizer = () => {
  const [summary, setSummary] = useState(" ")
  const [file, setFile] = useState([])
  const classes = useStyles();

  const sendFile = (event) => {
    setFile(event.target.files[0]) 

    const fileData = new FormData()
    fileData.append('file', file)
    console.log("hellooo")
    axios({
      method: 'post',
      url: 'http://127.0.0.1:5000/upload-file', 
      data: fileData,
      headers: {'Content-Type': 'multipart/form-data' }
    })
    .then(res => {
        setSummary(res.data)
        console.log(res.data)
        console.log("success")
    })
    .catch(err => {
        console.log("we have uh oh" + err)
    });
  }


  return (
    <Box className={classes.container}>
      <Box mt={5} mb={10}>
        <input
          accept="image/*"
          className={classes.input}
          id="contained-button-file"
          multiple
          type="file"
          onChange={sendFile}
        />
        <label htmlFor="contained-button-file">
          <Button variant="contained" color="primary" component="span">
            Upload
          </Button>
        </label>
      </Box>
      <Box borderRadius={10} mb={5} px={5} color="white" width="80%" bgcolor='text.secondary'>
        <Typography variant='h6'> {summary} </Typography>
      </Box>
    </Box>
  );
}

export default Summarizer