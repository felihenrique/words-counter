import axios from "axios";

const wordsApi = axios.create({ 
  baseURL: 'http://localhost:7600'
})

export default wordsApi;