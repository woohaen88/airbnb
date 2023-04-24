import react, { useEffect } from "react";
import useUser from "../lib/useUser";
import { useNavigate } from "react-router-dom";

// 사용자가 로그인을 했는지만 확인
//    - 먄약 로그인을 안했다면 우회
//    - 로그인을 했다면 제대로 출력

interface IProtectedPageProps {
  children: React.ReactNode;
}

export default function ProtectedPage({ children }: IProtectedPageProps) {
  const { user, isLoggedIn, userLoading } = useUser();
  const navigate = useNavigate();
  useEffect(() => {
    if (!userLoading) {
      if (!isLoggedIn) {
        navigate("/");
      }
    }
  }, [userLoading, isLoggedIn, navigate]);
  return <>{children}</>;
}
