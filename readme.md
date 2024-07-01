### fork本仓库代码

### 1.生成密钥对

在你的本地计算机上打开终端并运行以下命令：

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

名词说明：

- `-t rsa`：指定密钥类型为 RSA。
- `-b 4096`：指定密钥长度为 4096 位。
- `-C "your_email@example.com"`：为密钥添加一个标签，通常是你的电子邮件地址。

当被提示时：

- **文件保存位置**：按回车键使用默认位置（通常是 `~/.ssh/id_rsa`）。
- **密码短语**：可以选择设置密码短语来保护私钥，也可以按回车键跳过。

这将生成两个文件：

- `~/.ssh/id_rsa`：私钥。
- `~/.ssh/id_rsa.pub`：公钥。

### 2. 将公钥上传到服务器

将生成的公钥 `~/.ssh/id_rsa.pub` 内容复制到你的远程服务器的 `~/.ssh/authorized_keys` 文件中。你可以使用以下命令：

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub your_user@your_host
```

或者进入`后台管理面板`-`文件管理器`，在主目录下创建`.ssh`目录，然后在`.ssh`目录下新建文件，文件名为`authorized_keys`,将生成的公钥内容复制到`authorized_keys`文件内容里面

### 配置 GitHub Secrets

1. **进入 GitHub 仓库的设置：**

   - 打开你的 GitHub 仓库。
   - 点击右上角的 `Settings`。

2. **添加新的机密：**

   - 在左侧菜单中找到 `Secrets and variables`，然后选择 `Actions`。
   - 点击 `New repository secret` 按钮。

3. **添加机密值：**

| 变量           | 说明            | 示例                                                         |
| -------------- | --------------- | ------------------------------------------------------------ |
| SSH_HOST       | 主机名          | s5.serv00.com                                                |
| SSH_USER       | 用户名          | user                                                         |
| SSH_KEY        | 生成的私钥      | -----BEGIN OPENSSH PRIVATE KEY-----<br />HU03i/Qxrctssj1k5vg9jfWJNwwOXAM<br />bLdSLR4+bshKe7ffS7ZXkOQWdsadsd<br />-----END OPENSSH PRIVATE KEY----- |
| PUSHPLUS_TOKEN | pushplus的token | 41f7b1c60f2d584874b7d5bfa19a61c                             |

   



### 3. 触发工作流程

部署好后你可以手动触发该工作流程试运行一次：

- **手动触发：**
  - 进入 GitHub 仓库的 `Actions` 页面。
  - 选择 `serv00 login` 工作流程。
  - 点击 `Run workflow` 按钮。
  - 微信收到推送通知则表明已经成功配置并且可以正常运行
- **定时任务：**
  - 默认工作流程设置的定时任务为（每 30 天的上午 10 点）自动运行。可以根据你的实际情况修改
    

```yaml
- cron: '0 10 */30 * *' 
```

