import {
  VStack,
  Box,
  Image,
  Button,
  Grid,
  Text,
  HStack,
  useColorModeValue,
} from "@chakra-ui/react";

import { FaRegHeart, FaStar } from "react-icons/fa";

export default function Room() {
  const gray = useColorModeValue("gray.600", "gray.300");
  return (
    <VStack alignItems={"flex-start"}>
      <Box position="relative" overflow={"hidden"} mb={2} rounded="3xl">
        <Image
          minH="280"
          src="https://a0.muscache.com/im/pictures/d6880d5f-2d42-49eb-b3d3-366b9d285d6c.jpg?im_w=1200"
        />
        <Button
          variant={"unstyled"}
          position="absolute"
          top={0}
          right={0}
          color="white"
        >
          <FaRegHeart size="20" />
        </Button>
      </Box>
      <Box>
        <Grid gap={2} templateColumns={"6fr 1fr"}>
          <Text display={"block"} as="b" noOfLines={1} fontSize="sm">
            Mù cang chải , Yên Bái, 베트남
          </Text>
          <HStack spacing={1}>
            <FaStar size={15} />
            <Text>5.0</Text>
          </HStack>
        </Grid>
        <Text fontSize={"sm"} color={gray}>
          Seoul, S. Korea
        </Text>
      </Box>
      <Text fontSize={"sm"} color={gray}>
        <Text as="b">$72</Text>/night
      </Text>
    </VStack>
  );
}
