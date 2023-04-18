import {
  VStack,
  Grid,
  Box,
  Image,
  Text,
  HStack,
  Button,
} from "@chakra-ui/react";
import { FaStar, FaRegHeart } from "react-icons/fa";
import Room from "../Room";

// Grid
//   parameters:
//     templateColumns
//     gap
//     columnGap
//     rowGap

//     ex:) templateColumns={"200px 200px 200px ..."}
//          templateColumns={"repeat(5, 1fr)"} // 같은 비율로 5개
//          gap={10}
//          columnGap={4}
//          rowGap={8}
//          templateColumns={"2fr 1fr"} // 첫번째 칼럼이 두번째 칼럼의 2배

export default function Home() {
  return (
    <Grid
      mt={10}
      px={{
        base: 10,
        lg: 40,
      }}
      columnGap={4}
      rowGap={8}
      templateColumns={{
        base: "1fr",
        md: "1fr 1fr",
        lg: "repeat(3, 1fr)",
        xl: "repeat(4, 1fr)",
        "2xl": "repeat(5, 1fr)",
      }}
    >
      {[
        1, 2, 3, 13, 12, 31, 23, 123, 1, 31, 23, 123, 1, 321, 23, 12, 3, 123,
        12, 3, 13, 12, 31, 23, 123, 12, 312, 3, 123, 123, 1, 2, 3, 1, 1, 2, 3,
        4, 1, 2, 3, 1, 2, 3, 3,
      ].map((index) => (
        <Room key={index} />
      ))}
    </Grid>
  );
}
