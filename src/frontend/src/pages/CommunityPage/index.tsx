import { useContext, useEffect, useState } from "react";
import { GithubIcon, Users2, GitFork } from "lucide-react";
import { TabsContext } from "../../contexts/tabsContext";
import { alertContext } from "../../contexts/alertContext";
import { Button } from "../../components/ui/button";

import { getExamples } from "../../controllers/API";
import { FlowType } from "../../types/flow";
import { CardComponent } from "../../components/cardComponent";
import { useNavigate } from "react-router-dom";
export default function CommunityPage() {
  const { flows, setTabId, downloadFlows, uploadFlows, addFlow } =
    useContext(TabsContext);
  useEffect(() => {
    setTabId("");
  }, []);
  const { setErrorData } = useContext(alertContext);
  const [loadingExamples, setLoadingExamples] = useState(false);
  const [examples, setExamples] = useState<FlowType[]>([]);
  function handleExamples() {
    setLoadingExamples(true);
    getExamples()
      .then((result) => {
        setLoadingExamples(false);
        setExamples(result);
      })
      .catch((error) =>
        setErrorData({
          title: "there was an error loading examples, please try again",
          list: [error.message],
        })
      );
  }
  const navigate = useNavigate();

  useEffect(() => {
    handleExamples();
  }, []);
  return (
    <div className="w-full h-full flex overflow-auto flex-col bg-muted px-16">
      <div className="w-full flex justify-between py-12 pb-2 px-6">
        <span className="text-2xl flex items-center justify-center gap-2 font-semibold">
          <Users2 className="w-6" />
          社区示例
        </span>
        <div className="flex gap-2">
          <a
            href="https://github.com/logspace-ai/langflow_examples"
            target="_blank"
            rel="noreferrer"
          >
            <Button variant="primary">
              <GithubIcon className="w-4 mr-2" />
              添加示例
            </Button>
          </a>
        </div>
      </div>
      <span className="flex pb-8 px-6 w-[70%] text-muted-foreground">
         发现并学习社区的共享示例。欢迎贡献帮助我们的社区探索新的强大功能的示例。
      </span>
      <div className="w-full p-4 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {!loadingExamples &&
          examples.map((flow, idx) => (
            <CardComponent
              key={idx}
              flow={flow}
              id={flow.id}
              button={
                <Button
                  variant="outline"
                  size="sm"
                  className="whitespace-nowrap "
                  onClick={() => {
                    addFlow(flow, true).then((id) => {
                      navigate("/flow/" + id);
                    });
                  }}
                >
                  <GitFork className="w-4 mr-2" />
                  Fork Example
                </Button>
              }
            />
          ))}
      </div>
    </div>
  );
}
