import { Alert, Button, Grid } from "@mui/material";
import { WordsTextInput } from "./styles";
import WordsTable from "./WordsTable";
import useGetWordsData from "../../hooks/useGetWordsData";
import { useState } from "react";

const MainScreen = () => {
  const [textQuery, setTextQuery] = useState("");
  const { isLoading, data, error } = useGetWordsData(textQuery);
  const [text, setText] = useState("");

  return (
    <Grid container padding={5}>
      <Grid item xs={12}>
        <WordsTextInput
          value={text}
          onChange={(event) => setText(event.target.value)}
          multiline
          fullWidth
          label="Text to count"
          rows={6}
        />
        <Button
          onClick={() => setTextQuery(text)}
          disabled={isLoading}
          variant="contained"
        >
          Count words
        </Button>
        {error && <Alert severity="error">{error}</Alert>}
      </Grid>
      <Grid item xs={6} marginTop={2}>
        <WordsTable words={data} isLoading={isLoading} />
      </Grid>
    </Grid>
  );
};

export default MainScreen;
