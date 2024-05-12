import { useEffect, useState } from "react";

interface Props<T> {
  value: T;
  delay?: number;
}

function useDebounce<T>({ value, delay }: Props<T>) {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay ?? 500);

    return () => {
      clearTimeout(timer);
    };
  }, [value, delay]);

  return debouncedValue;
}

export default useDebounce;
