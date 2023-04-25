import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { getRoom, getRoomReviews } from "../../api";
import { IRoomDetail, IRoomReview } from "../../types";
import {
  Box,
  Grid,
  GridItem,
  HStack,
  Heading,
  Image,
  Skeleton,
  VStack,
  Text,
  Avatar,
  Container,
} from "@chakra-ui/react";
import { FaStar } from "react-icons/fa";

export default function RoomDetail() {
  const { roomId } = useParams();
  const { isLoading, data } = useQuery<IRoomDetail>([`rooms`, roomId], getRoom);
  const { data: reviewsData, isLoading: isReviewsLoading } =
    useQuery<IRoomReview>([`rooms`, roomId, `reviews`], getRoomReviews);

  return (
    <Box
      mt={10}
      px={{
        base: 10,
        lg: 40,
      }}
    >
      <Skeleton w={"75%"} height={"43px"} isLoaded={!isLoading}>
        <Heading>{data?.name}</Heading>
      </Skeleton>
      <Grid
        mt={8}
        rounded={"2xl"}
        overflow={"hidden"}
        gap={2}
        height={"60vh"}
        templateRows={"1fr 1fr"}
        templateColumns={"repeat(4, 1fr)"}
      >
        {[0, 1, 2, 3, 4].map((index) => (
          <GridItem
            colSpan={index === 0 ? 2 : 1}
            rowSpan={index === 0 ? 2 : 1}
            overflow={"hidden"}
            key={index}
          >
            <Skeleton isLoaded={!isLoading} h={"100%"} w={"100%"}>
              {data?.photos && data.photos.length > 0 ? (
                <Image
                  objectFit={"cover"}
                  w={"100%"}
                  h={"100%"}
                  src={data?.photos[index].file}
                />
              ) : null}
            </Skeleton>
          </GridItem>
        ))}
      </Grid>
      <HStack mt={10} w={"40%"} justifyContent={"space-between"}>
        <VStack alignItems={"flex-start"}>
          <Skeleton isLoaded={!isLoading}>
            <Heading fontSize={"xl"}>
              House hosted by {data?.owner.username}
            </Heading>
          </Skeleton>
          <Skeleton isLoaded={!isLoading}>
            <HStack justifyContent={"flex-start"} w={"100%"}>
              <Text>
                {data?.toilets} toilet{data?.toilets === 1 ? "" : "s"}
              </Text>
              <Text>•</Text>
              <Text>
                {data?.rooms} room{data?.rooms === 1 ? "" : "s"}
              </Text>
            </HStack>
          </Skeleton>
        </VStack>

        <Avatar
          size={"xl"}
          name={data?.owner.username}
          src="https://play-lh.googleusercontent.com/PCpXdqvUWfCW1mXhH1Y_98yBpgsWxuTSTofy3NGMo9yBTATDyzVkqU580bfSln50bFU"
        />
      </HStack>
      <Box mt={10}>
        <Skeleton isLoaded={!isReviewsLoading} w={"18%"}>
          <Heading mb={5} fontSize={"2xl"}>
            <HStack>
              <FaStar /> <Text>{data?.rating}</Text>
              <Text>·</Text>
              <Text>{reviewsData?.results.length}</Text>
              <Text>review{reviewsData?.results.length === 1 ? "" : "s"} </Text>
            </HStack>
          </Heading>
        </Skeleton>
        <Container mt={15} maxW={"container.lg"} marginX={"none"}>
          <Grid gap={10} templateColumns={"1fr 1fr"}>
            {reviewsData?.results.map((review, index) => (
              <VStack alignItems={"flex-start"} key={index}>
                <HStack spacing={"1"}>
                  <Avatar name={review.user.username} size="md" />
                  <VStack alignItems={"flex-start"}>
                    <Heading fontSize={"md"}>{review.user.username}</Heading>
                    <HStack spacing={"1"}>
                      <FaStar size={"12px"} />
                      <Text>{review.rating}</Text>
                    </HStack>
                  </VStack>
                </HStack>
                <Text>{review.payload}</Text>
              </VStack>
            ))}
          </Grid>
        </Container>
      </Box>
    </Box>
  );
}

// note:
// 60vh : 사용자 화면의 60%
