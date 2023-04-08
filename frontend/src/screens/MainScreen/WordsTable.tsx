import {
  Paper,
  Skeleton,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow
} from "@mui/material";
import { NoDataText } from "./styles";
import { Word } from "../../interfaces/word";

export interface WordsTableProps {
  words: Word[];
  isLoading?: boolean;
}

const WordsTable: React.FC<WordsTableProps> = ({ words, isLoading }) => {
  return (
    <Table component={Paper} size="small">
      <TableHead>
        <TableCell>World title</TableCell>
        <TableCell>Quantity</TableCell>
      </TableHead>
      <TableBody>
        {isLoading && <Skeleton variant="rectangular" />}
        {!isLoading && words.length == 0 && (
          <NoDataText>
            No words to show. Please the text box to input your text and click
            count words.
          </NoDataText>
        )}
        {words &&
          words.map((word) => (
            <TableRow>
              <TableCell>{word.title}</TableCell>
              <TableCell>{word.quantity}</TableCell>
            </TableRow>
          ))}
      </TableBody>
    </Table>
  );
};

export default WordsTable;
