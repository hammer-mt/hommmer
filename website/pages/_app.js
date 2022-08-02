import "tailwindcss/tailwind.css";

import TagManager from "react-gtm-module";
import { useEffect } from "react";

function MyApp({ Component, pageProps }) {
  const tagManagerArgs = {
    gtmId: "GTM-P24ZPZM",
  };
  useEffect(() => {
    TagManager.initialize(tagManagerArgs);
  }, []);

  return <Component {...pageProps} />;
}

export default MyApp;
