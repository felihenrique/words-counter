import { useCallback, useEffect, useState } from "react";
import axios from "axios";
import wordsApi from "../api/words";
import { Word } from "../interfaces/word";

interface ResponseType {
  [word: string]: number
}

const useGetWordsData = (text: string) => {
  const [data, setData] = useState<Word[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string>('');

  const getData = useCallback(async (textInput: string) => {
    if(textInput === '') {
      return [];
    }

    try {
      setIsLoading(true);
      setError('');
      const { data } = await wordsApi.post<ResponseType>("/words/count", {
        text: textInput,
        lang: "en",
      });
      const mappedData: Word[] = Object.entries(data).map(([key, value]) => ({
        title: key,
        quantity: value,
      }));
      setData(mappedData);
    } catch(err: any) {
      setData([]);
      setError(err.message)
    } finally {
      setIsLoading(false);
    }
  }, [setData, setIsLoading]);

  useEffect(() => {
    getData(text);
  }, [text]);

  return { data, error, isLoading };
};

export default useGetWordsData;
