import React, { type FC, type ReactNode } from "react";
import "./style.scss"
import useIsMobile from "../../hooks/useIsMobile";

interface Props {
  children: ReactNode;
  transparentBackground?: boolean;
}

const PageContainer: FC<Props> = ({ children, transparentBackground }) => {
  const { isMobile } = useIsMobile();

  return (
    <div
      className={`page-container ${
        isMobile ? "mobile-page-container" : "desktop-page-container"
      }`}
      style={transparentBackground ? { background: "transparent" } : undefined}
    >
      {children}
    </div>
  );
};

export default PageContainer;
