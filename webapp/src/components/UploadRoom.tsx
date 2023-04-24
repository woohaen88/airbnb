import HostOnlyPage from "./HostOnlyPage";
import ProtectedPage from "./ProtectedPage";

export default function UploadRoom() {
  return (
    <ProtectedPage>
      <HostOnlyPage>
        <h1>upload form</h1>;
      </HostOnlyPage>
    </ProtectedPage>
  );
}
