import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, TextField, Button, Typography } from "@mui/material";

function ThreeT() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    tone: "",
    topic: "",
    target: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    alert("Form submitted!");
    navigate("/home");
  };

  return (
    <Box
      sx={{
        maxWidth: 400,
        mx: "auto",
        mt: 5,
        p: 3,
        border: "1px solid #eee",
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <Typography variant="h5" align="center" gutterBottom>
        3T information
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          fullWidth
          label="Tone"
          name="tone"
          value={form.tone}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          label="Topic"
          name="topic"
          type="text"
          value={form.topic}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          label="Target"
          name="target"
          //   type="tel"
          value={form.target}
          onChange={handleChange}
          margin="normal"
          required
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          fullWidth
          sx={{ mt: 2 }}
        >
          Submit
        </Button>
      </form>
    </Box>
  );
}

export default ThreeT;
