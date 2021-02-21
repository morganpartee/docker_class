import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Container, Grid, TextField, Typography, AppBar, Toolbar } from '@material-ui/core';

function App() {
  const [sepalLength, setSepalLength] = useState();
  const [sepalWidth, setSepalWidth] = useState();
  const [petalLength, setPetalLength] = useState();
  const [petalWidth, setPetalWidth] = useState();
  const [prediction, setPrediction] = useState("");

  const checkFloat = (n) => {
    const floatedN = parseFloat(n);
    return isNaN(floatedN) ? null : floatedN
  }

  const handlePrediction = () => {
    axios.post("http://localhost:8000/predict", {
      sepal_len: sepalLength,
      sepal_wid: sepalWidth,
      petal_len: petalLength,
      petal_wid: petalWidth
    }).then((res) => setPrediction(res.data))
  }

  return (
    <Container disableGutters>
      <AppBar position="static" >
        <Toolbar>
          <Typography variant="h5">
            Iris Hardcore ML
          </Typography>
        </Toolbar>
      </AppBar>
      <Container container>
        <Typography variant="h6">Enter your flower shape and get a prize!</Typography>
        <Grid justify="stretch">
          <TextField value={sepalLength} label="Sepal Length" onChange={(e) => setSepalLength(checkFloat(e.target.value))} />
          <TextField value={sepalWidth} label="Sepal Width" onChange={(e) => setSepalWidth(checkFloat(e.target.value))} />
          <TextField value={petalLength} label="Petal Length" onChange={(e) => setPetalLength(checkFloat(e.target.value))} />
          <TextField value={petalWidth} label="Petal Width" onChange={(e) => setPetalWidth(checkFloat(e.target.value))} />
          <Button onClick={handlePrediction}>Submit</Button>
          {
            prediction && (
              <Typography variant="h4">{prediction}</Typography>
            )
          }
        </Grid>
      </Container>
    </Container>
  );
}

export default App;
