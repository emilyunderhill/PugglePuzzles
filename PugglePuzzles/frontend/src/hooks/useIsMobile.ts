import { useEffect, useState } from "react";

const useIsMobile = () => {
  const [isMobile, setIsMobile] = useState(
    window.matchMedia("(max-width: 768px)").matches
  );

  useEffect(() => {
    setIsMobile(window.matchMedia("(max-width: 768px)").matches);
  }, [window.innerWidth]);

  return {
    isMobile,
  };
};

export default useIsMobile
