# AI Chat System Design

## Architecture Overview

The AI chat system integrates OpenAI's API with Convex for real-time data synchronization, providing a seamless chat experience with streaming responses and persistent conversation history.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Chat Client   │    │     Convex      │    │    OpenAI API   │
│   (React UI)    │◄──►│   Real-time     │◄──►│   Chat Models   │
│                 │    │   Database      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐              │
         └─────────────►│  File Storage   │◄─────────────┘
                        │   & Processing  │
                        └─────────────────┘
```

## Data Model Design

### Convex Schema

#### Conversations Table
```typescript
conversations: defineTable({
  userId: v.string(),                    // User ID from Clerk
  title: v.string(),                     // Conversation title
  createdAt: v.number(),                 // Creation timestamp
  updatedAt: v.number(),                 // Last update timestamp
  isArchived: v.optional(v.boolean()),   // Archive status
  tags: v.optional(v.array(v.string())), // Conversation tags
  metadata: v.optional(v.object({        // Additional metadata
    model: v.string(),                   // AI model used
    totalTokens: v.number(),             // Total tokens used
    messageCount: v.number(),            // Number of messages
  })),
})
.index("userId", ["userId"])
.index("createdAt", ["createdAt"])
.index("userId_updatedAt", ["userId", "updatedAt"])
```

#### Messages Table
```typescript
messages: defineTable({
  conversationId: v.id("conversations"), // Reference to conversation
  role: v.union(v.literal("user"), v.literal("assistant"), v.literal("system")),
  content: v.string(),                   // Message content
  createdAt: v.number(),                 // Message timestamp
  status: v.union(                       // Message status
    v.literal("sending"),
    v.literal("sent"), 
    v.literal("streaming"),
    v.literal("completed"),
    v.literal("failed")
  ),
  metadata: v.optional(v.object({        // Message metadata
    tokens: v.optional(v.number()),      // Token count
    model: v.optional(v.string()),       // Model used
    finishReason: v.optional(v.string()), // Completion reason
    attachments: v.optional(v.array(v.id("files"))), // File attachments
  })),
})
.index("conversationId", ["conversationId"])
.index("createdAt", ["createdAt"])
```

#### Files Table
```typescript
files: defineTable({
  userId: v.string(),                    // Owner user ID
  conversationId: v.optional(v.id("conversations")), // Associated conversation
  filename: v.string(),                  // Original filename
  contentType: v.string(),               // MIME type
  size: v.number(),                      // File size in bytes
  storageId: v.id("_storage"),           // Convex storage ID
  uploadedAt: v.number(),                // Upload timestamp
  processedAt: v.optional(v.number()),   // Processing completion
  metadata: v.optional(v.object({        // File metadata
    extractedText: v.optional(v.string()), // Extracted text content
    imageAnalysis: v.optional(v.any()),   // Image analysis results
    processingStatus: v.string(),         // Processing status
  })),
})
.index("userId", ["userId"])
.index("conversationId", ["conversationId"])
```

## Component Architecture

### 1. Chat Interface Components

#### Chat Layout (`app/routes/dashboard/chat.tsx`)
- **Purpose**: Main chat page layout and state management
- **Responsibilities**:
  - Manage conversation selection and creation
  - Handle real-time message updates
  - Coordinate between sidebar and message area
  - Manage chat settings and preferences

#### Chat Sidebar (`app/components/chat/chat-sidebar.tsx`)
- **Purpose**: Conversation list and management
- **Responsibilities**:
  - Display conversation history
  - Handle conversation search and filtering
  - Provide conversation actions (delete, archive, export)
  - Show conversation metadata and previews

#### Message Area (`app/components/chat/message-area.tsx`)
- **Purpose**: Main message display and interaction area
- **Responsibilities**:
  - Render conversation messages
  - Handle message streaming display
  - Manage scroll position and virtual scrolling
  - Show typing indicators and status

#### Message Input (`app/components/chat/message-input.tsx`)
- **Purpose**: Message composition and sending
- **Responsibilities**:
  - Handle text input with rich formatting
  - Manage file uploads and attachments
  - Send messages and handle responses
  - Show input status and validation

### 2. Message Components

#### Message Bubble (`app/components/chat/message-bubble.tsx`)
- **Purpose**: Individual message display
- **Responsibilities**:
  - Render user and AI messages differently
  - Support markdown formatting
  - Handle message actions (copy, edit, delete)
  - Show message metadata and status

#### Streaming Message (`app/components/chat/streaming-message.tsx`)
- **Purpose**: Real-time streaming message display
- **Responsibilities**:
  - Display partial messages as they stream
  - Handle streaming interruption and resumption
  - Show streaming progress indicators
  - Manage streaming state and cleanup

#### Message Attachments (`app/components/chat/message-attachments.tsx`)
- **Purpose**: File attachment display and management
- **Responsibilities**:
  - Preview different file types
  - Handle file download and sharing
  - Show file processing status
  - Manage attachment interactions

## AI Integration Design

### 1. OpenAI API Integration

#### Chat Service (`app/lib/chat-service.ts`)
```typescript
interface ChatService {
  sendMessage(params: {
    messages: ChatMessage[];
    model?: string;
    stream?: boolean;
    onStream?: (chunk: string) => void;
  }): Promise<ChatResponse>;
  
  processFile(file: File): Promise<ProcessedFile>;
  
  generateTitle(messages: ChatMessage[]): Promise<string>;
}

class OpenAIChatService implements ChatService {
  private client: OpenAI;
  
  constructor(apiKey: string) {
    this.client = new OpenAI({ apiKey });
  }
  
  async sendMessage(params: SendMessageParams): Promise<ChatResponse> {
    const stream = await this.client.chat.completions.create({
      model: params.model || 'gpt-4',
      messages: params.messages,
      stream: params.stream || false,
    });
    
    if (params.stream) {
      return this.handleStreamingResponse(stream, params.onStream);
    }
    
    return this.handleResponse(stream);
  }
}
```

#### Streaming Handler (`app/lib/streaming-handler.ts`)
```typescript
class StreamingHandler {
  private controller: AbortController;
  private onChunk: (chunk: string) => void;
  private onComplete: (message: string) => void;
  private onError: (error: Error) => void;
  
  async handleStream(
    stream: AsyncIterable<ChatCompletionChunk>,
    callbacks: StreamingCallbacks
  ): Promise<void> {
    let fullMessage = '';
    
    try {
      for await (const chunk of stream) {
        if (this.controller.signal.aborted) {
          break;
        }
        
        const content = chunk.choices[0]?.delta?.content || '';
        if (content) {
          fullMessage += content;
          callbacks.onChunk(content);
        }
      }
      
      callbacks.onComplete(fullMessage);
    } catch (error) {
      callbacks.onError(error as Error);
    }
  }
  
  abort(): void {
    this.controller.abort();
  }
}
```

### 2. Convex Functions for Chat

#### Message Management (`convex/messages.ts`)
```typescript
export const sendMessage = mutation({
  args: {
    conversationId: v.id("conversations"),
    content: v.string(),
    attachments: v.optional(v.array(v.id("files"))),
  },
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) throw new Error("Unauthorized");
    
    // Insert user message
    const messageId = await ctx.db.insert("messages", {
      conversationId: args.conversationId,
      role: "user",
      content: args.content,
      createdAt: Date.now(),
      status: "sent",
      metadata: {
        attachments: args.attachments,
      },
    });
    
    // Update conversation timestamp
    await ctx.db.patch(args.conversationId, {
      updatedAt: Date.now(),
    });
    
    return messageId;
  },
});

export const streamAIResponse = action({
  args: {
    conversationId: v.id("conversations"),
    messages: v.array(v.any()),
  },
  handler: async (ctx, args) => {
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
    
    // Create AI message placeholder
    const aiMessageId = await ctx.runMutation(api.messages.createAIMessage, {
      conversationId: args.conversationId,
    });
    
    try {
      const stream = await openai.chat.completions.create({
        model: "gpt-4",
        messages: args.messages,
        stream: true,
      });
      
      let fullContent = '';
      
      for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content || '';
        if (content) {
          fullContent += content;
          
          // Update message with streaming content
          await ctx.runMutation(api.messages.updateStreamingMessage, {
            messageId: aiMessageId,
            content: fullContent,
            status: "streaming",
          });
        }
      }
      
      // Mark message as completed
      await ctx.runMutation(api.messages.completeMessage, {
        messageId: aiMessageId,
        content: fullContent,
      });
      
    } catch (error) {
      await ctx.runMutation(api.messages.markMessageFailed, {
        messageId: aiMessageId,
        error: error.message,
      });
    }
  },
});
```

#### Conversation Management (`convex/conversations.ts`)
```typescript
export const createConversation = mutation({
  args: {
    title: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) throw new Error("Unauthorized");
    
    const conversationId = await ctx.db.insert("conversations", {
      userId: identity.subject,
      title: args.title || "New Conversation",
      createdAt: Date.now(),
      updatedAt: Date.now(),
      metadata: {
        model: "gpt-4",
        totalTokens: 0,
        messageCount: 0,
      },
    });
    
    return conversationId;
  },
});

export const getUserConversations = query({
  args: {
    limit: v.optional(v.number()),
    cursor: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) return [];
    
    const conversations = await ctx.db
      .query("conversations")
      .withIndex("userId_updatedAt", (q) => 
        q.eq("userId", identity.subject)
      )
      .order("desc")
      .take(args.limit || 50);
    
    return conversations;
  },
});
```

## Real-time Communication Design

### 1. Message Streaming Architecture

```typescript
// Client-side streaming handler
class MessageStreamer {
  private eventSource: EventSource | null = null;
  private onMessage: (content: string) => void;
  private onComplete: () => void;
  private onError: (error: Error) => void;
  
  startStreaming(conversationId: string, callbacks: StreamingCallbacks) {
    this.onMessage = callbacks.onMessage;
    this.onComplete = callbacks.onComplete;
    this.onError = callbacks.onError;
    
    // Use Convex action for streaming
    this.initiateStream(conversationId);
  }
  
  private async initiateStream(conversationId: string) {
    try {
      // Trigger Convex action that handles OpenAI streaming
      await convex.mutation(api.messages.streamAIResponse, {
        conversationId,
        messages: this.getConversationMessages(),
      });
    } catch (error) {
      this.onError(error as Error);
    }
  }
  
  stopStreaming() {
    if (this.eventSource) {
      this.eventSource.close();
      this.eventSource = null;
    }
  }
}
```

### 2. Real-time Updates with Convex

```typescript
// React hook for real-time conversation updates
function useConversationMessages(conversationId: string) {
  const messages = useQuery(api.messages.getConversationMessages, {
    conversationId,
  });
  
  const [streamingMessage, setStreamingMessage] = useState<string>('');
  const [isStreaming, setIsStreaming] = useState(false);
  
  // Subscribe to real-time message updates
  useEffect(() => {
    if (!conversationId) return;
    
    const unsubscribe = convex.onUpdate(
      api.messages.getConversationMessages,
      { conversationId },
      (newMessages) => {
        const lastMessage = newMessages[newMessages.length - 1];
        
        if (lastMessage?.status === 'streaming') {
          setStreamingMessage(lastMessage.content);
          setIsStreaming(true);
        } else if (lastMessage?.status === 'completed') {
          setIsStreaming(false);
          setStreamingMessage('');
        }
      }
    );
    
    return unsubscribe;
  }, [conversationId]);
  
  return {
    messages: messages || [],
    streamingMessage,
    isStreaming,
  };
}
```

## File Upload and Processing Design

### 1. File Upload Handler

```typescript
// File upload service
class FileUploadService {
  async uploadFile(
    file: File,
    conversationId?: string
  ): Promise<UploadedFile> {
    // Validate file
    this.validateFile(file);
    
    // Upload to Convex storage
    const storageId = await convex.mutation(api.files.generateUploadUrl);
    
    const response = await fetch(storageId.uploadUrl, {
      method: 'POST',
      body: file,
    });
    
    if (!response.ok) {
      throw new Error('Upload failed');
    }
    
    // Create file record
    const fileId = await convex.mutation(api.files.createFile, {
      filename: file.name,
      contentType: file.type,
      size: file.size,
      storageId: storageId.storageId,
      conversationId,
    });
    
    // Process file for AI context
    await this.processFile(fileId);
    
    return { id: fileId, url: response.url };
  }
  
  private validateFile(file: File): void {
    const maxSize = 10 * 1024 * 1024; // 10MB
    const allowedTypes = [
      'text/plain',
      'text/markdown',
      'application/pdf',
      'image/jpeg',
      'image/png',
      'image/webp',
    ];
    
    if (file.size > maxSize) {
      throw new Error('File too large');
    }
    
    if (!allowedTypes.includes(file.type)) {
      throw new Error('File type not supported');
    }
  }
}
```

### 2. File Processing Pipeline

```typescript
// Convex action for file processing
export const processFile = action({
  args: { fileId: v.id("files") },
  handler: async (ctx, args) => {
    const file = await ctx.runQuery(api.files.getFile, {
      fileId: args.fileId,
    });
    
    if (!file) throw new Error("File not found");
    
    const fileUrl = await ctx.storage.getUrl(file.storageId);
    if (!fileUrl) throw new Error("File URL not available");
    
    let processedData: any = {};
    
    try {
      switch (file.contentType) {
        case 'text/plain':
        case 'text/markdown':
          processedData.extractedText = await this.extractTextFromFile(fileUrl);
          break;
          
        case 'application/pdf':
          processedData.extractedText = await this.extractTextFromPDF(fileUrl);
          break;
          
        case 'image/jpeg':
        case 'image/png':
        case 'image/webp':
          processedData.imageAnalysis = await this.analyzeImage(fileUrl);
          break;
      }
      
      // Update file with processed data
      await ctx.runMutation(api.files.updateFileMetadata, {
        fileId: args.fileId,
        metadata: {
          ...processedData,
          processingStatus: 'completed',
        },
        processedAt: Date.now(),
      });
      
    } catch (error) {
      await ctx.runMutation(api.files.updateFileMetadata, {
        fileId: args.fileId,
        metadata: {
          processingStatus: 'failed',
          error: error.message,
        },
      });
    }
  },
});
```

## Security and Privacy Design

### 1. API Key Management

```typescript
// Secure API key handling
class APIKeyManager {
  private static instance: APIKeyManager;
  private apiKey: string;
  
  private constructor() {
    this.apiKey = process.env.OPENAI_API_KEY!;
    
    if (!this.apiKey) {
      throw new Error('OpenAI API key not configured');
    }
  }
  
  static getInstance(): APIKeyManager {
    if (!APIKeyManager.instance) {
      APIKeyManager.instance = new APIKeyManager();
    }
    return APIKeyManager.instance;
  }
  
  getAPIKey(): string {
    return this.apiKey;
  }
  
  // Rotate API key (for production key rotation)
  rotateKey(newKey: string): void {
    this.apiKey = newKey;
  }
}
```

### 2. Content Filtering and Safety

```typescript
// Content moderation service
class ContentModerationService {
  private openai: OpenAI;
  
  constructor(apiKey: string) {
    this.openai = new OpenAI({ apiKey });
  }
  
  async moderateContent(content: string): Promise<ModerationResult> {
    try {
      const moderation = await this.openai.moderations.create({
        input: content,
      });
      
      const result = moderation.results[0];
      
      return {
        flagged: result.flagged,
        categories: result.categories,
        categoryScores: result.category_scores,
      };
    } catch (error) {
      console.error('Content moderation failed:', error);
      // Fail safe - allow content but log for review
      return { flagged: false, categories: {}, categoryScores: {} };
    }
  }
  
  async filterMessage(message: string): Promise<string> {
    const moderation = await this.moderateContent(message);
    
    if (moderation.flagged) {
      throw new Error('Message contains inappropriate content');
    }
    
    return message;
  }
}
```

## Performance Optimization

### 1. Message Virtualization

```typescript
// Virtual scrolling for large conversation histories
function VirtualizedMessageList({ messages }: { messages: Message[] }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [visibleRange, setVisibleRange] = useState({ start: 0, end: 50 });
  
  const itemHeight = 100; // Estimated message height
  const containerHeight = 600; // Container height
  
  const handleScroll = useCallback((event: React.UIEvent) => {
    const scrollTop = event.currentTarget.scrollTop;
    const start = Math.floor(scrollTop / itemHeight);
    const visibleCount = Math.ceil(containerHeight / itemHeight);
    
    setVisibleRange({
      start: Math.max(0, start - 5), // Buffer
      end: Math.min(messages.length, start + visibleCount + 5),
    });
  }, [messages.length]);
  
  const visibleMessages = messages.slice(visibleRange.start, visibleRange.end);
  
  return (
    <div
      ref={containerRef}
      className="message-list"
      style={{ height: containerHeight, overflowY: 'auto' }}
      onScroll={handleScroll}
    >
      <div style={{ height: visibleRange.start * itemHeight }} />
      {visibleMessages.map((message, index) => (
        <MessageBubble
          key={message.id}
          message={message}
          style={{ height: itemHeight }}
        />
      ))}
      <div style={{ 
        height: (messages.length - visibleRange.end) * itemHeight 
      }} />
    </div>
  );
}
```

### 2. Intelligent Caching

```typescript
// Message and conversation caching
class ChatCache {
  private conversationCache = new Map<string, Conversation>();
  private messageCache = new Map<string, Message[]>();
  
  cacheConversation(conversation: Conversation): void {
    this.conversationCache.set(conversation.id, conversation);
  }
  
  getCachedConversation(id: string): Conversation | undefined {
    return this.conversationCache.get(id);
  }
  
  cacheMessages(conversationId: string, messages: Message[]): void {
    this.messageCache.set(conversationId, messages);
  }
  
  getCachedMessages(conversationId: string): Message[] | undefined {
    return this.messageCache.get(conversationId);
  }
  
  invalidateConversation(id: string): void {
    this.conversationCache.delete(id);
    this.messageCache.delete(id);
  }
  
  clear(): void {
    this.conversationCache.clear();
    this.messageCache.clear();
  }
}
```