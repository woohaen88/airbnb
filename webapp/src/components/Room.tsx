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
import React from "react";

import { FaCamera, FaRegHeart, FaStar } from "react-icons/fa";
import { Link, useNavigate } from "react-router-dom";

interface IRoomProps {
  imageUrl: string;
  name: string;
  rating: number;
  city: string;
  country: string;
  price: number;
  id: number;
  isOwner: boolean;
}

export default function Room({
  id,
  imageUrl,
  name,
  rating,
  city,
  country,
  price,
  isOwner,
}: IRoomProps) {
  const gray = useColorModeValue("gray.600", "gray.300");
  const navigate = useNavigate();
  const onCameraClick = (event: React.SyntheticEvent<HTMLButtonElement>) => {
    event.preventDefault();
    navigate(`/room/${id}/photos`);
  };

  return (
    <Link to={`/room/${id}`}>
      <VStack alignItems={"flex-start"}>
        <Box position="relative" overflow={"hidden"} mb={2} rounded="3xl">
          <Image
            minH={{
              sm: "330",
              md: "330",
              lg: "330",
              xl: "330",
              "2xl": "330",
            }}
            src={imageUrl}
            objectFit={"cover"}
          />

          <Button
            variant={"unstyled"}
            position="absolute"
            top={0}
            right={0}
            color="white"
            onClick={onCameraClick}
          >
            {isOwner ? <FaCamera size={"20"} /> : <FaRegHeart size="20" />}
          </Button>
        </Box>
        <Box>
          <Grid gap={2} templateColumns={"6fr 1fr"}>
            <Text display={"block"} as="b" noOfLines={1} fontSize="sm">
              {name}
            </Text>
            <HStack spacing={1}>
              <FaStar size={15} />
              <Text>{rating}</Text>
            </HStack>
          </Grid>
          <Text fontSize={"sm"} color={gray}>
            {city}, {country}
          </Text>
        </Box>
        <Text fontSize={"sm"} color={gray}>
          <Text as="b">${price}</Text>/night
        </Text>
      </VStack>
    </Link>
  );
}
