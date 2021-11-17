import Head from "next/head";
import { useState, useRef } from "react";
import { DuplicateIcon, CheckIcon } from "@heroicons/react/solid";

export default function Home() {
  const copyAreaRef = useRef(null);
  const [copiedText, setCopiedText] = useState("");

  const quickStartInstructions = [
    { title: "Install the package", code: "pip install hommmer" },
    { title: "Import the library", code: "import hommmer as mmm" },
    {
      title: "Build your model",
      code: "media = ['facebook', 'google', 'tiktok']\nmodel = mmm.build('duff.csv', 'sales', media)",
    },
    { title: "Display the results", code: "model.show()" },
  ];

  const handleClickToCopy = (text) => {
    copyAreaRef.current.value = text;
    copyAreaRef.current.select();
    document.execCommand("copy");
    copyAreaRef.current.value = "";
    copyAreaRef.current.blur();
    setCopiedText(text);
  };
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <Head>
        <title>
          hommmer: A simple Marketing Mix Modeling library in Python.
        </title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="flex flex-col items-center justify-center flex-1 text-center">
        <div className="bg-skin-yellow rounded-xl py-12">
          <h1 className="mx-auto text-4xl font-bold bg-white rounded-xl py-3 px-6 w-min">
            <a
              href="https://github.com/hammer-mt/hommmer"
              className="hover:text-donut-pink"
            >
              hommmer
            </a>
          </h1>

          <p className="bg-stubble-brown p-3 rounded-xl mt-9 text-2xl w-2/3 mx-auto font-medium">
            A simple Marketing Mix Modeling library in Python.
          </p>
        </div>

        <div className="p-9 mt-6 text-left border-2 w-full rounded-xl">
          <h3 className="text-2xl font-bold">Quick Start</h3>

          {quickStartInstructions.map((instruction) => {
            return (
              <>
                <p className="mt-6 text-xl">{instruction.title}:</p>
                <div
                  className="group cursor-pointer"
                  onClick={() => {
                    handleClickToCopy(instruction.code);
                  }}
                >
                  <div className="flex items-center">
                    <code className="font-mono bg-gray-100 p-3 my-3 whitespace-pre">
                      {instruction.code}
                    </code>
                    {copiedText === instruction.code ? (
                      <CheckIcon
                        className="h-6 w-6 ml-2 text-gray-400 invisible group-hover:visible"
                        aria-hidden="true"
                      />
                    ) : (
                      <DuplicateIcon
                        className="h-6 w-6 ml-2 text-gray-400 invisible group-hover:visible"
                        aria-hidden="true"
                      />
                    )}
                  </div>
                </div>
              </>
            );
          })}

          <textarea
            style={{
              opacity: ".01",
              height: 1,
              width: 1,
              position: "absolute",
              zIndex: -9999,
            }}
            ref={copyAreaRef}
          ></textarea>
        </div>

        <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
          <a
            href="https://pypi.org/project/hommmer/"
            className="bg-pants-blue p-6 mt-6 text-left border w-96 rounded-xl hover:bg-donut-pink hover:text-white"
          >
            <h3 className="text-2xl font-bold">Documentation &rarr;</h3>
            <p className="mt-4 text-xl">
              Learn how to use <code className="font-mono">hommmer</code> for
              marketing mix modeling.
            </p>
          </a>

          <a
            href="https://app.vexpower.com/courses/"
            className="bg-pants-blue p-6 mt-6 text-left border w-96 rounded-xl hover:bg-donut-pink hover:text-white"
          >
            <h3 className="text-2xl font-bold">Tutorials &rarr;</h3>
            <p className="mt-4 text-xl">
              Learn about marketing mix modeling in simulator-based courses.
            </p>
          </a>

          <a
            href="https://github.com/hammer-mt/hommmer"
            className="bg-pants-blue p-6 mt-6 text-left border w-96 rounded-xl hover:bg-donut-pink hover:text-white"
          >
            <h3 className="text-2xl font-bold">GitHub &rarr;</h3>
            <p className="mt-4 text-xl">
              Take a look at the code in our GitHub repository and contribute.
            </p>
          </a>

          <a
            href="https://discord.gg/nE6gHxMwXC"
            className="bg-pants-blue p-6 mt-6 text-left border w-96 rounded-xl hover:bg-donut-pink hover:text-white"
          >
            <h3 className="text-2xl font-bold">Discord &rarr;</h3>
            <p className="mt-4 text-xl">
              Join users and contributors in our Discord community.
            </p>
          </a>
        </div>
      </main>

      <footer className="flex bg-shoe-black text-white p-6 items-center justify-center h-24 mt-12 rounded-xl space-x-6">
        <div className="flex w-48 items-center justify-center">
          Open Source{" "}
          <a
            className="flex items-center justify-center mx-1 hover:text-donut-pink focus:text-donut-pink"
            href="https://github.com/hammer-mt/hommmer/blob/main/LICENSE"
            target="_blank"
            rel="noopener noreferrer"
          >
            MIT License
          </a>
        </div>
        <div className="flex w-48 items-center justify-center">
          Built by{" "}
          <a
            className="flex items-center justify-center mx-1 hover:text-donut-pink focus:text-donut-pink"
            href="https://twitter.com/hammer_mt"
            target="_blank"
            rel="noopener noreferrer"
          >
            @hammer_mt
          </a>
        </div>
      </footer>
    </div>
  );
}
