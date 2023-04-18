import { Fragment } from "react";
import {
  BriefcaseIcon,
  CalendarIcon,
  CheckIcon,
  ChevronDownIcon,
  CurrencyDollarIcon,
  LinkIcon,
  MapPinIcon,
  PencilIcon,
} from "@heroicons/react/20/solid";
import { Menu, Transition } from "@headlessui/react";

function classNames(...classes: any) {
  return classes.filter(Boolean).join(" ");
}
import Box from "@mui/material/Box";

import React, { useState } from "react";
import Slider from "@mui/material/Slider";

export default function Home() {
  const [sliderValue, setSliderValue] = useState([20, 80]);

  const handleSliderChange = (event: any, newValue: any) => {
    setSliderValue(newValue);
  };

  return (
    <>
      <div className="px-4 py-16 sm:px-6 lg:px-8 bg-indigo-200 h-48">
        <div className="flex items-center gap-x-8">
          <Slider
            value={sliderValue}
            onChange={handleSliderChange}
            aria-labelledby="range-slider"
            marks={[
              {
                value: 0,
                label: "0%",
              },
              {
                value: 100,
                label: "100%",
              },
            ]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
            sx={{
              width: "calc(100% - 48px)",
              marginLeft: "24px",
              marginRight: "24px",
            }}
            className="w-full"
          />
        </div>
      </div>
    </>
  );
}
