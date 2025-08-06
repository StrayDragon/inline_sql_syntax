# GitHub Actions for VSCode Extension

本项目包含两个GitHub Actions工作流，用于自动化VSCode扩展的打包和发布流程。

## 工作流说明

### 1. Package VSIX (`package-vsix.yml`)

**触发条件：**
- 推送到 `main`、`master` 或 `develop` 分支
- 针对 `main` 或 `master` 分支的Pull Request
- 手动触发

**功能：**
- 自动构建和打包扩展为 `.vsix` 文件
- 将打包好的文件作为构建产物上传，保留7天
- 适用于开发阶段的持续集成

### 2. Package and Release (`package-and-release.yml`)

**触发条件：**
- 推送带有版本标签的提交（如 `v1.0.0`）
- 手动触发（可指定版本号和是否为预发布版本）

**功能：**
- 打包扩展为 `.vsix` 文件
- 自动发布到 Visual Studio Marketplace
- 自动发布到 Open VSX Registry
- 创建GitHub Release并附加 `.vsix` 文件

## 配置要求

### 必需的Secrets

在GitHub仓库的Settings > Secrets and variables > Actions中添加以下secrets：

1. **VS_MARKETPLACE_TOKEN**
   - Visual Studio Marketplace的Personal Access Token
   - 获取方式：访问 [Azure DevOps](https://dev.azure.com/) → User Settings → Personal Access Tokens
   - 权限：Marketplace (Manage)

2. **OPEN_VSX_TOKEN**
   - Open VSX Registry的Access Token
   - 获取方式：访问 [Open VSX Registry](https://open-vsx.org/) → 登录 → Access Tokens

### 版本发布流程

#### 方法1：使用Git标签（推荐）

```bash
# 更新package.json中的版本号
npm version patch  # 或 minor, major

# 推送标签
git push origin --tags
```

#### 方法2：手动触发

1. 访问GitHub仓库的Actions页面
2. 选择"Package and Release Extension"工作流
3. 点击"Run workflow"
4. 输入版本号和是否为预发布版本
5. 点击"Run workflow"开始执行

## 工作流特性

### 最新实践

- 使用最新的GitHub Actions版本（v4）<mcreference link="https://github.com/marketplace/actions/publish-vs-code-extension" index="1">1</mcreference>
- 支持pnpm包管理器
- 使用HaaLeo/publish-vscode-extension进行发布<mcreference link="https://github.com/marketplace/actions/publish-vs-code-extension" index="1">1</mcreference>
- 自动生成Release Notes
- 支持预发布版本

### 构建产物

- 每次构建都会生成 `.vsix` 文件作为构建产物
- 开发构建保留7天，发布构建永久保留
- 可直接下载用于本地测试

### 多平台发布

- 同时发布到Visual Studio Marketplace和Open VSX Registry<mcreference link="https://github.com/marketplace/actions/publish-vs-code-extension" index="1">1</mcreference>
- 确保扩展在VS Code和其他兼容编辑器中都可用

## 故障排除

### 常见问题

1. **构建失败**
   - 检查package.json中的scripts是否正确
   - 确保所有依赖都已正确安装

2. **发布失败**
   - 验证Personal Access Token是否有效
   - 检查版本号是否符合语义化版本规范
   - 确保package.json中的publisher字段正确

3. **权限错误**
   - 确保GitHub Token有足够权限创建Release
   - 检查Marketplace Token的权限设置

### 调试建议

- 先使用"Package VSIX"工作流测试构建过程
- 检查构建产物是否正确生成
- 在本地测试 `.vsix` 文件的安装

## 参考资源

- [VS Code Extension API - Publishing](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)<mcreference link="https://code.visualstudio.com/api/working-with-extensions/publishing-extension" index="3">3</mcreference>
- [HaaLeo/publish-vscode-extension Action](https://github.com/marketplace/actions/publish-vs-code-extension)<mcreference link="https://github.com/marketplace/actions/publish-vs-code-extension" index="1">1</mcreference>
- [Visual Studio Code Extension Manager (vsce)](https://github.com/microsoft/vscode-vsce)