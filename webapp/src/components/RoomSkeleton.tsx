import { Box, Skeleton, Grid, SkeletonText } from "@chakra-ui/react";

export default function RoomSkeleton() {
  return (
    <Box>
      <Skeleton rounded="2xl" height={280} mb={3} />

      <Grid gap={1} templateColumns={"4fr 1fr"}>
        <SkeletonText skeletonHeight={"4"} pt={2} noOfLines={1} />
        <SkeletonText skeletonHeight={"4"} pt={2} noOfLines={1} />
      </Grid>
      <Box w={"40%"}>
        <SkeletonText skeletonHeight={"4"} pt={2} noOfLines={1} />
      </Box>

      <Box w={"30%"}>
        <SkeletonText skeletonHeight={"4"} pt={3} noOfLines={1} />
      </Box>
    </Box>
  );
}
