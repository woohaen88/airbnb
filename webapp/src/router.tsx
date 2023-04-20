import { createBrowserRouter } from "react-router-dom";
import Root from "./components/Root";
import Home from "./components/routes/Home";
import NotFound from "./components/routes/NotFound";
import RoomDetail from "./components/routes/RoomDetail";
import GithubConfirm from "./components/routes/GithubConfirm";
const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <NotFound />,
    children: [
      {
        path: "",
        element: <Home />,
      },
      {
        path: "room/:roomId",
        element: <RoomDetail />,
      },
      {
        path: "social/github",
        element: <GithubConfirm />,
      },
    ],
  },
]);

export default router;
