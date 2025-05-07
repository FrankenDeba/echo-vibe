import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, TextField, Button, Typography } from "@mui/material";

/*
 name = business_profile.name
        industry = business_profile.industry
        description = business_profile.description
        uniqueness = business_profile.uniqueness
        tagline = business_profile.tagline
*/

function BusinessDescription() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    industry: "",
    description: "",
    uniqueness: "",
    tagline: "",
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
    navigate("/3t");
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
        Business Description
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          fullWidth
          multiline
          label="name"
          name="name"
          value={form.name}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          label="industry"
          name="industry"
          type="text"
          value={form.industry}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          multiline
          label="description"
          name="description"
          //   type="tel"
          value={form.description}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          multiline
          label="uniqueness"
          name="uniqueness"
          type="text"
          value={form.uniqueness}
          onChange={handleChange}
          margin="normal"
          required
        />
        <TextField
          fullWidth
          label="tagline"
          name="tagline"
          type="text"
          value={form.tagline}
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

export default BusinessDescription;
