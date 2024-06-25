Streamlit 框架主要通过以下几种方式识别和处理路由：

## 1. 多页面应用的路由识别
Streamlit 提供了多页面应用的支持，允许开发者在一个应用中创建多个页面。每个页面都有四个标识部分：页面源代码、页面标签、页面标题和 URL 路径名。Streamlit 会根据这些标识来生成页面的 URL 路径名。例如，如果页面的标识符来自文件名，Streamlit 会将文件名中的连续空格和下划线压缩为一个下划线，并将其用作 URL 路径名[1]。

### URL 路径名生成规则
- 如果页面的标识符来自文件名，Streamlit 会将连续的空格和下划线压缩为一个下划线。
- 如果页面的标识符来自可调用函数名，Streamlit 会直接使用该标识符。
- 如果页面有编号但没有标识符，Streamlit 会使用编号作为路径名。

例如，如果应用在 `localhost:8501` 运行，名为 `Awesome_page.py` 的页面的完整 URL 将是 `localhost:8501/awesome_page`[1]。

## 2. 使用 Streamlit-Router 进行路由管理
Streamlit-Router 是一个第三方库，提供了更高级的路由管理功能。它允许开发者定义更复杂的多页面应用，并支持通过 URL 传递参数。Streamlit-Router 提供了一个干净的语法和接口，使得多页面开发变得非常简单[2]。

### 示例代码
```python
from streamlit_router import StreamlitRouter

def index(router):
    st.text("首页")
    x = st.number_input("任务 ID")
    if st.button("创建任务"):
        router.redirect(*router.build("create_task", {"x": x}))
    if st.button("取消任务"):
        router.redirect(*router.build("cancel_task", {"x": x}))
    if st.button("查看任务"):
        router.redirect(*router.build("view_task", {"x": x}))

def cancel_task(router, x):
    st.text(f"取消任务 x={x}")
    if st.button("返回首页"):
        router.redirect(*router.build("index"))

def create_task(x, router):
    st.text(f"创建任务 x={x}")
    if st.button("返回首页"):
        router.redirect(*router.build("index"))

router = StreamlitRouter()
router.register(index, '/')
router.register(cancel_task, "/tasks/<int:x>", methods=['DELETE'])
router.register(create_task, "/tasks/<int:x>", methods=['POST'])

@router.map("/tasks/<int:x>")
def view_task(x):
    st.text(f"查看任务 x={x}")
    if st.button("返回首页"):
        router.redirect(*router.build("index"))

router.serve()
```
这个示例展示了如何使用 Streamlit-Router 定义和管理多页面应用的路由[2]。

## 3. 使用 Streamlit 内置的多页面支持
Streamlit 还提供了内置的多页面支持，开发者可以通过创建 `pages/` 目录并在其中添加页面文件来实现多页面应用。Streamlit 会自动识别这些页面并在导航菜单中显示它们[1]。

### 示例代码
```python
# 在 pages 目录下创建多个页面文件，例如 page1.py 和 page2.py
# page1.py
import streamlit as st

st.title("这是页面 1")

# page2.py
import streamlit as st

st.title("这是页面 2")
```
在这种方式下，Streamlit 会自动生成页面的 URL 路径名，并在导航菜单中显示页面标签[1]。

综上所述，Streamlit 框架通过文件名、函数名和第三方库（如 Streamlit-Router）来识别和管理路由，使得开发者可以轻松创建和管理多页面应用。

Citations:
[1] https://docs.streamlit.io/develop/concepts/multipage-apps/overview
[2] https://discuss.streamlit.io/t/new-component-streamlit-router-allows-you-to-create-truly-production-level-multi-page-applications/67633
[3] https://datatunnel.io/tldr_listing/streamlit-app-framework-tutorial-and-deployment-guide/
[4] https://github.com/maxmarkov/streamlit-navigator
[5] https://streamlit.io
[6] https://discuss.streamlit.io/t/is-there-a-way-to-have-multiple-pages-like-flask/16823
[7] https://towardsdatascience.com/designing-operations-research-solutions-a-user-friendly-routing-application-with-streamlit-17212553861d?gi=e00980f4552a
[8] https://discuss.streamlit.io/t/how-to-plot-map-routes-obtained-from-azure-maps/2314
[9] https://github.com/ntt-dkiku/route-explainer
[10] https://discuss.streamlit.io/t/shortest-route-visualizer/12889
[11] https://speakerdeck.com/nearme_tech/dynamic-vehicle-routing-nosimiyuresiyonwo-streamlitdezuo-tutemita
[12] https://discuss.streamlit.io/t/streamlit-homepage-url/45651