# MVP Agent 项目

## 项目概览

本项目是一个 **MVP 级别的全栈智能 Agent 系统**，功能包括：

- **前端控制台**：使用 React + Tailwind 构建，可实时查看和管理任务  
- **后端服务**：FastAPI 提供 REST API 接口  
- **多 Agent 调度**：使用 Celery + Redis 实现任务队列和异步执行  
- **数据库**：SQLite，用于存储任务状态和历史记录  
- **通知**：飞书 Webhook 占位  
- **容器化部署**：通过 Docker Compose 部署前后端、Redis、Celery  

## 目录结构

```plain text
mvp_agent_project/
├─ backend/
│  ├─ main.py
│  ├─ agents.py
│  ├─ tasks.py
│  ├─ database.py
│  ├─ notifications.py
│  ├─ requirements.txt
├─ frontend/
│  ├─ package.json
│  ├─ tailwind.config.js
│  └─ src/
│      ├─ index.jsx
│      ├─ App.jsx
│      └─ api.js
├─ docker-compose.yml
└─ README.md
```


## 安装与运行

### 1. 前端

```
cd frontend
npm install
npm run build
```

### 2. 后端 & Celery & Redis

使用 Docker Compose 启动：

```
docker-compose up --build
```

- **FastAPI** 后端服务：`http://localhost:8000`  
- **前端控制台**：`http://localhost:3000`  

## 功能说明

### 前端控制台

- 输入 Agent 名称，点击 **运行 Agent**  
- 列表展示所有任务状态，包括 `pending`, `running`, `done`  
- 显示任务结果和通知信息  

### 后端 API

- **POST /api/run_agent**：创建任务并调度 Agent  
- **GET /api/tasks**：获取任务列表和状态  

### 多 Agent 调度

- 每个任务通过 **Celery** 异步执行  
- 任务完成后更新 **SQLite** 数据库  
- 调用 **飞书 Webhook** 占位发送通知  

### 数据库（SQLite）

- 表 `tasks`：
  - `id`：任务 ID  
  - `name`：Agent 名称  
  - `status`：任务状态 (`pending`, `running`, `done`)  
  - `result`：任务结果  

## 技术栈

- **前端**：React, TailwindCSS  
- **后端**：FastAPI, Python  
- **异步任务**：Celery + Redis  
- **数据库**：SQLite  
- **容器化**：Docker Compose  
- **通知**：飞书 Webhook 占位  

## 使用示例

1. 通过控制台输入 Agent 名称 `TestAgent`  
2. 点击运行  
3. 在任务列表中查看状态：

```
1 | TestAgent | running | 
2 | TestAgent | done | TestAgent completed successfully
```

4. 控制台可模拟收到飞书通知：

```
[Feishu Notification] 任务完成: TestAgent, ID: 2
```

## 下一步扩展

- 接入真实 GPT Agent，支持自动任务生成和多 Agent 协作  
- 增加用户权限管理和前端界面优化  
- 集成真正飞书 Webhook 通知  
