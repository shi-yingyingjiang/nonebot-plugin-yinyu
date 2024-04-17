import yinglish
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import ArgPlainText ,CommandArg
from nonebot.plugin import PluginMetadata



__plugin_meta__ = PluginMetadata(
    name='淫语',
    description='把语句变成淫语',
    usage='淫语',
    extra={}
)



body = on_command("淫语")


@body.handle()
async def handle_first_receive(arg: Message = CommandArg()):
    if substance := arg.extract_plain_text():
        yingyu_substance = yinglish.chs2yin(substance)
        await body.finish(f"{yingyu_substance}")


@body.got("substance", prompt="请输入要转化的语句")
async def got_substance(substance: str = ArgPlainText()):
    yinyu_substance = yinglish.chs2yin(substance)
    await body.finish(f"{yinyu_substance}")